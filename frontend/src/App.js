import { Routes, Route, BrowserRouter } from "react-router-dom";

import "./App.css";

import Login from "./pages/loginSignup/Login";
import Signup from "./pages/loginSignup/Signup";
import AddPlayer from "./pages/Dashboard/Players/AddPlayer";
import Players from "./pages/Dashboard/Players/Players";
import ContentUnits from "./pages/Dashboard/ContentUnits/ContentUnits";
import AddContentUnit from "./pages/Dashboard/ContentUnits/AddContentUnit";
import Videos from "./pages/Dashboard/Videos/Videos";
import AddVideos from "./pages/Dashboard/Videos/AddVideos";
import EditPlayer from "./pages/Dashboard/Players/EditPlayer";
import Playlist from "./pages/Dashboard/Playlist/Playlist";
import AddPlaylist from "./pages/Dashboard/Playlist/AddPlaylist";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import axios from "axios";
import { setSessionUser } from "./slices/sessionSlice";

function App() {
  const dispatch = useDispatch();

  useEffect(() => {
    const getUser = async () => {
      axios
        .get(`/api/session/getSession`)
        .then(({ data }) => {
          dispatch(setSessionUser(data));
        })
        .catch((err) => {
          console.log(err);
        });
    };

    getUser();
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Login />} />
        <Route exact path="/dashboard" element={<Players />} />
        <Route exact path="/addPlayer" element={<AddPlayer />} />
        <Route exact path="/editPlayer" element={<EditPlayer />} />
        <Route exact path="/contentUnits" element={<ContentUnits />} />
        <Route exact path="/addContentUnit" element={<AddContentUnit />} />
        <Route exact path="/videos" element={<Videos />} />
        <Route exact path="/addVideos" element={<AddVideos />} />
        <Route exact path="/playlists" element={<Playlist />} />
        <Route exact path="/addPlaylists" element={<AddPlaylist />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
