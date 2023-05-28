import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
// import Test from "./Test";

const playerId = document.currentScript.getAttribute("playerId");
const playlistId = document.currentScript.getAttribute("playlistId");
const videoplayer = ReactDOM.createRoot(document.getElementById("videoplayer"));
videoplayer.render(
  <React.StrictMode>
    <App playerId={playerId} playlistId={playlistId} />
  </React.StrictMode>
);

// const root = ReactDOM.createRoot(document.getElementById("root"));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );
