# DjanGIS Front End

A modern, dark-themed Single Page Application (SPA) for viewing and interacting with spatial data.

## Features

### 🎨 Modern Dark UI
- Sleek, dark theme optimized for extended use
- Inter font for clean, modern typography
- Smooth animations and transitions
- Responsive design for mobile and desktop

### 🗺️ Interactive Map
- CartoDB Dark Matter base tiles
- Real-time coordinate display
- Zoom level indicator
- Click features for detailed information

### 📊 Layer Management
- Dynamic layer loading from API
- Visual indicators for layer access permissions
- One-click layer toggling
- Layer information panel
- Automatic zoom to layer bounds

### 🔐 Integrated Authentication
- Session-based authentication
- Login/logout functionality
- Permission-based layer access
- Visual indicators for restricted layers

### 🚀 Performance
- Asynchronous data loading
- Client-side rendering
- Efficient layer management
- Toast notifications for user feedback

## Usage

1. **Login** (if required):
   - Click the "Login" button in the header
   - Use your credentials to access restricted layers

2. **View Layers**:
   - Available layers appear in the left sidebar
   - Public layers are accessible to everyone
   - Restricted layers show a disabled state if you don't have access

3. **Toggle Layers**:
   - Click any accessible layer to add it to the map
   - Click again to remove it
   - Active layers show a green status indicator

4. **Interact with Features**:
   - Click on map features to see their properties
   - Use mouse wheel or zoom controls to navigate
   - Coordinates update as you move the mouse

5. **Refresh Data**:
   - Click the refresh button in the sidebar header
   - Layers will reload from the server

## Technical Stack

- **Leaflet.js**: Interactive map library
- **Vanilla JavaScript**: No framework dependencies
- **CSS3**: Modern styling with CSS variables
- **Django Templates**: Server-side rendering of the app shell

## Architecture

The frontend follows a hybrid approach:
- Django serves the initial HTML shell with authentication state
- All subsequent interactions are handled client-side
- API calls fetch GeoJSON data dynamically
- No page reloads required after initial load

## Customization

### Changing the Theme

Edit CSS variables in `app.css`:
```css
:root {
    --bg-primary: #0a0a0a;
    --accent-primary: #4a9eff;
    /* ... */
}
```

### Map Configuration

Edit defaults in `app.js`:
```javascript
DEFAULT_CENTER: [39.7392, -104.9903], // Your location
DEFAULT_ZOOM: 10,
```

### Adding New Features

The app structure is modular:
- `App.init()`: Application initialization
- `App.loadLayers()`: Layer management
- `App.toggleLayer()`: Layer interaction
- `App.showToast()`: User notifications 