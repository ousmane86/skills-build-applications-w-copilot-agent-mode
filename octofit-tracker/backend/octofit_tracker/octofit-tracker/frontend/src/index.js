
// Ensure REACT_APP_CODESPACE_NAME is set for API URLs
if (!process.env.REACT_APP_CODESPACE_NAME) {
  console.warn('REACT_APP_CODESPACE_NAME is not set. API calls may fail.');
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
