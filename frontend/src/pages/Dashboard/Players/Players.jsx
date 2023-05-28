import React, { useEffect, useState } from "react";
import "./Players.css";
import Navbar from "../../../components/Navbar/Navbar";
import Sidebar from "../../../components/Sidebar/Sidebar";
import playIcon from "../../../assets/play-button-icon.jpg";
import BorderColorIcon from "@mui/icons-material/BorderColor";
import AssessmentIcon from "@mui/icons-material/Assessment";
import DeleteIcon from "@mui/icons-material/Delete";
import { Link } from "react-router-dom";
import axios from "axios";

export default function Players() {
  const [players, setPlayers] = useState([]);

  // const getPlayers = async () => {
  //   await axios
  //     .get(`http://64.227.170.236/player/get/post/api/`)
  //     .then(({ data }) => {
  //       setPlayers(data);
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     });
  // };

  const getPlayers = async () => {
    await axios
      .get(`/api/player/getPlayers`)
      .then(({ data }) => {
        setPlayers(data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    getPlayers();
  }, []);

  // const handleDelete = async (id) => {
  //   await axios
  //     .delete(`http://64.227.170.236/player/update/delete/api/${id}/`)
  //     .then((res) => {
  //       getPlayers();
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     });
  // };

  const handleDelete = async (id) => {
    await axios
      .put(`/api/player/deletePlayer`, { playerId: id })
      .then((res) => {
        getPlayers();
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="palyers">
      <Navbar />
      <div className="palyers-main">
        <Sidebar />
        <div className="palyers-main-container">
          <Link to="/addPlayer" className="newPlayerButton">
            Add New Player
          </Link>
          <div className="programsContainer">
            {players.map((e, index) => {
              return (
                <div className="programsBox" key={index}>
                  <img className="playIcon" src={playIcon} alt=""></img>
                  <div className="programsBox-main">
                    <div className="programsBox-title-div">
                      <span className="programsBox-title">{e.playerName}</span>
                      <div className="programsBox-button-div">
                        <Link className="programsBox-button" to="/editPlayer" state={players.filter((p) => p._id.toString() === e._id.toString())}>
                          Edit
                        </Link>
                      </div>
                    </div>
                    <div style={{ margin: "5px 0px", display: "flex", alignItems: "center" }}>
                      <span>Player Id: {e._id}</span>
                    </div>

                    <span className="programBox-details">
                      <Link to="/dashboard" className="link">
                        <li className="sidebarListItem active">
                          <BorderColorIcon className="sidebarIcon" />
                        </li>
                      </Link>
                      <Link to="/pendingApprovalsAdmin" className="link">
                        <li className="sidebarListItem">
                          <AssessmentIcon className="sidebarIcon" />
                        </li>
                      </Link>

                      <li className="sidebarListItem" onClick={() => handleDelete(e._id)}>
                        <DeleteIcon className="sidebarIcon" />
                      </li>
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
