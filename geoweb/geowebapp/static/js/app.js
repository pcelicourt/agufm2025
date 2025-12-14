// Main Application Object
// Version: 1.1 - Fixed API response handling
const App = {
    // Application state
    map: null,
    layers: {},
    activeLayers: {},
    
    // API endpoints
    API_BASE: '/api',
    
    // Map configuration
    //DEFAULT_CENTER: [39.7392, -104.9903], // Denver, Colorado
    DEFAULT_ZOOM: 10,
    
    // Initialize the application
    async init() {
        console.log('🚀 Initializing DjanGIS...');
        
        // Initialize the map
        //this.initMap();
        
        // Load layers from API
        await this.loadLayers();
        
        // Setup event listeners
        this.setupEventListeners();
        
        // Initialize UI updates
        this.initUIUpdates();
        
        console.log('✅ DjanGIS initialized successfully');
    },
    
    // Initialize Leaflet map
    initMap() {
        // Create map instance
        this.map = L.map('map', {
            center: this.DEFAULT_CENTER,
            zoom: this.DEFAULT_ZOOM,
            zoomControl: false
        });
        
        // Add custom zoom control to top-left
        L.control.zoom({
            position: 'topleft'
        }).addTo(this.map);
        
        // Add dark tile layer (CartoDB Dark Matter)
        L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
            subdomains: 'abcd',
            maxZoom: 20
        }).addTo(this.map);
        
        // Update coordinates on mouse move
        this.map.on('mousemove', (e) => {
            document.getElementById('coordinates').textContent = 
                `Lat: ${e.latlng.lat.toFixed(4)}, Lng: ${e.latlng.lng.toFixed(4)}`;
        });
        
        // Update zoom level
        this.map.on('zoomend', () => {
            document.getElementById('zoom-info').textContent = 
                `Zoom: ${this.map.getZoom()}`;
        });
    },
    
    // Load layers from API
    async loadLayers() {
        const layerList = document.getElementById('layer-list');
        
        try {
            const response = await fetch(`${this.API_BASE}/layers/`);
            if (!response.ok) throw new Error('Failed to fetch layers');
            
            const data = await response.json();
            this.layers = {};
            
            // Clear loading state
            layerList.innerHTML = '';
            
            // Handle both array and paginated responses
            const layers = Array.isArray(data) ? data : (data.results || []);
            
            if (layers.length === 0) {
                layerList.innerHTML = '<p class="hint">No layers available</p>';
                return;
            }
            
            // Render each layer
            layers.forEach(layer => {
                this.layers[layer.id] = layer;
                const layerElement = this.createLayerElement(layer);
                layerList.appendChild(layerElement);
            });
            
        } catch (error) {
            console.error('Error loading layers:', error);
            layerList.innerHTML = '<p class="hint">Error loading layers</p>';
            this.showToast('Failed to load layers', 'error');
        }
    },
    
    // Create layer element for sidebar
    createLayerElement(layer) {
        const div = document.createElement('div');
        div.className = 'layer-item';
        div.dataset.layerId = layer.id;
        
        // Add disabled class if user doesn't have access
        if (!layer.has_access) {
            div.classList.add('disabled');
        }
        
        div.innerHTML = `
            <div>
                <div class="layer-name">${layer.display_name}</div>
                <div class="layer-type">${layer.layer_type}</div>
            </div>
            <div class="layer-status"></div>
        `;
        
        // Add click handler
        if (layer.has_access) {
            div.addEventListener('click', () => this.toggleLayer(layer.id));
        } else {
            div.title = 'Login required to access this layer';
            div.addEventListener('click', () => {
                this.showToast('Please login to access this layer', 'warning');
                // Optionally redirect to login
                if (confirm('Would you like to login now?')) {
                    window.location.href = '/accounts/login/?next=/';
                }
            });
        }
        
        return div;
    },
    
    // Toggle layer on/off
    async toggleLayer(layerId) {
        const layer = this.layers[layerId];
        if (!layer) return;
        
        const layerElement = document.querySelector(`[data-layer-id="${layerId}"]`);
        
        // Check if layer is already active
        if (this.activeLayers[layerId]) {
            // Remove layer
            if (layer.layer_type === 'raster') {
                // Remove all raster overlays
                this.activeLayers[layerId].forEach(overlay => {
                    this.map.removeLayer(overlay);
                });
            } else {
                this.map.removeLayer(this.activeLayers[layerId]);
            }
            delete this.activeLayers[layerId];
            layerElement.classList.remove('active');
            this.showToast(`${layer.display_name} removed`, 'success');
        } else {
            // Add layer
            try {
                layerElement.classList.add('loading');
                
                const response = await fetch(`${this.API_BASE}/layers/${layerId}/features/`);
                if (!response.ok) throw new Error('Failed to fetch features');
                
                const data = await response.json();
                
                if (layer.layer_type === 'raster' && data.type === 'RasterLayer') {
                    // Handle raster overlays
                    const overlays = [];
                    
                    if (!data.overlays || data.overlays.length === 0) {
                        this.showToast(`No raster overlays found in ${layer.display_name}`, 'warning');
                        layerElement.classList.remove('loading');
                        return;
                    }
                    
                    data.overlays.forEach(overlay => {
                        // Create image bounds
                        const bounds = [
                            [overlay.south, overlay.west],
                            [overlay.north, overlay.east]
                        ];
                        
                        // Create Leaflet image overlay
                        const imageOverlay = L.imageOverlay(overlay.image_url, bounds, {
                            opacity: overlay.opacity,
                            interactive: true
                        });
                        
                        // Add popup if overlay has a name
                        if (overlay.name) {
                            imageOverlay.bindPopup(`<h4>${overlay.name}</h4>`);
                        }
                        
                        // Handle rotation if needed (Leaflet doesn't support rotation natively)
                        // For now, we'll add without rotation
                        if (overlay.rotation !== 0) {
                            console.warn(`Rotation not supported for overlay: ${overlay.name}`);
                        }
                        
                        imageOverlay.addTo(this.map);
                        overlays.push(imageOverlay);
                    });
                    
                    this.activeLayers[layerId] = overlays;
                    
                    // Zoom to layer bounds if available
                    if (data.overlays.length > 0) {
                        const boundsResponse = await fetch(`${this.API_BASE}/layers/${layerId}/bounds/`);
                        if (boundsResponse.ok) {
                            const boundsData = await boundsResponse.json();
                            if (boundsData.bounds) {
                                const [west, south, east, north] = boundsData.bounds;
                                this.map.fitBounds([[south, west], [north, east]], { padding: [50, 50] });
                            }
                        }
                    }
                    
                } else {
                    // Handle vector features (existing code)
                    const leafletLayer = L.geoJSON(data, {
                        style: this.getFeatureStyle(layer.layer_type),
                        pointToLayer: this.createPointLayer,
                        onEachFeature: this.onEachFeature
                    });
                    
                    // Add to map
                    leafletLayer.addTo(this.map);
                    this.activeLayers[layerId] = leafletLayer;
                    
                    // Zoom to layer bounds
                    const bounds = leafletLayer.getBounds();
                    if (bounds.isValid()) {
                        this.map.fitBounds(bounds, { padding: [50, 50] });
                    }
                }
                
                layerElement.classList.add('active');
                this.showToast(`${layer.display_name} added`, 'success');
                
            } catch (error) {
                console.error('Error loading layer features:', error);
                this.showToast(`Failed to load ${layer.display_name}`, 'error');
            } finally {
                layerElement.classList.remove('loading');
            }
        }
        
        // Update layer info panel
        this.updateLayerInfo(layer);
    },
    
    // Get feature style based on layer type
    getFeatureStyle(layerType) {
        const styles = {
            polygon: {
                fillColor: '#4a9eff',
                fillOpacity: 0.2,
                color: '#4a9eff',
                weight: 2
            },
            line: {
                color: '#52c41a',
                weight: 3,
                opacity: 0.8
            },
            point: {
                radius: 8,
                fillColor: '#faad14',
                fillOpacity: 0.8,
                color: '#fff',
                weight: 2
            }
        };
        
        return styles[layerType] || styles.polygon;
    },
    
    // Create point layer with custom markers
    createPointLayer(feature, latlng) {
        return L.circleMarker(latlng, {
            radius: 8,
            fillColor: '#faad14',
            fillOpacity: 0.8,
            color: '#fff',
            weight: 2
        });
    },
    
    // Handle feature interactions
    onEachFeature(feature, layer) {
        if (feature.properties) {
            // Create popup content
            let popupContent = '<div class="feature-popup">';
            
            if (feature.properties.name) {
                popupContent += `<h4>${feature.properties.name}</h4>`;
            }
            
            // Add all properties
            Object.entries(feature.properties).forEach(([key, value]) => {
                if (key !== 'name' && value !== null) {
                    popupContent += `<p><strong>${key}:</strong> ${value}</p>`;
                }
            });
            
            popupContent += '</div>';
            
            layer.bindPopup(popupContent);
        }
    },
    
    // Update layer info panel
    updateLayerInfo(layer) {
        const infoPanel = document.getElementById('layer-info');
        
        infoPanel.innerHTML = `
            <h3>${layer.display_name}</h3>
            <p class="hint">${layer.description || 'No description available'}</p>
            <div style="margin-top: 1rem;">
                <p><strong>Type:</strong> ${layer.layer_type}</p>
                <p><strong>Features:</strong> ${layer.feature_count}</p>
                <p><strong>Access:</strong> ${layer.public ? 'Public' : 'Restricted'}</p>
            </div>
        `;
    },
    
    // Setup event listeners
    setupEventListeners() {
        // Refresh layers button
        document.getElementById('refresh-layers').addEventListener('click', async () => {
            this.showToast('Refreshing layers...', 'info');
            await this.loadLayers();
        });
    },
    
    // Initialize UI updates
    initUIUpdates() {
        // Set initial zoom level
        document.getElementById('zoom-info').textContent = 
            `Zoom: ${this.map.getZoom()}`;
    },
    
    // Show toast notification
    showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.textContent = message;
        
        const container = document.getElementById('toast-container');
        container.appendChild(toast);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            toast.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }
};

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    //App.init();
}); 