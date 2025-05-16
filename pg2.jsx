// App.jsx
import React from 'react';

const App = () => {
  return (
    <div className="flex justify-center p-4">
      <h1 className="text-2xl font-bold mb-4">Women Safety Analytics Dashboard</h1>
      <img src="http://localhost:5000/video_feed" alt="Live Feed" className="border-4 border-blue-500 rounded-lg" />
    </div>
  );
};

export default App;
