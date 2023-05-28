import "./sidebar.css";

import LiveTvIcon from "@mui/icons-material/LiveTv";
import EngineeringIcon from "@mui/icons-material/Engineering";
import SmartDisplayIcon from "@mui/icons-material/SmartDisplay";
import PlaylistPlayIcon from "@mui/icons-material/PlaylistPlay";

import { Link, useLocation } from "react-router-dom";

export default function Sidebar() {
  const location = useLocation();

  return (
    <div className="sidebar">
      <div className="sidebarWrapper">
        <div className="sidebarMenu">
          {/* <h3 className="sidebarTitle">Dashboard</h3> */}
          <ul className="sidebarList">
            <Link to="/videos" className="link">
              <li className="sidebarListItem" style={location.pathname === "/videos" ? { backgroundColor: "rgb(240, 240, 255)" } : null}>
                <SmartDisplayIcon className="sidebarIcon" />
                Videos
              </li>
            </Link>
            <Link to="/playlists" className="link">
              <li className="sidebarListItem" style={location.pathname === "/playlists" ? { backgroundColor: "rgb(240, 240, 255)" } : null}>
                <PlaylistPlayIcon className="sidebarIcon" />
                Playlists
              </li>
            </Link>
            <Link to="/" className="link">
              <li className="sidebarListItem" style={location.pathname === "/" ? { backgroundColor: "rgb(240, 240, 255)" } : null}>
                <LiveTvIcon className="sidebarIcon" />
                Players
              </li>
            </Link>
            <Link to="/contentUnits" className="link">
              <li className="sidebarListItem" style={location.pathname === "/contentUnits" ? { backgroundColor: "rgb(240, 240, 255)" } : null}>
                <EngineeringIcon className="sidebarIcon" />
                Content Units
              </li>
            </Link>
          </ul>
        </div>
      </div>
    </div>
  );
}
