import React from 'react';
import { createRoot } from 'react-dom/client';

export default function App() {
  return (
    <div>
      <header>
        <h1>Welcome to My Simple React Page</h1>
      </header>
      <p>This is a simple React page example.</p>
      <button>BUTTON</button>
      <div>
        <a href='/home'>home</a>
        <br></br>
        <a href='/about'>About</a>
      </div>

    </div>
  );
}

// Select the root element by ID and render the App component inside it
const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
root.render(<App />);
