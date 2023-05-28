import "./AddContentUnit.css";
import React, { useState } from "react";

import ReactPlayer from "react-player";
import { useEffect } from "react";
import Navbar from "../../../components/Navbar/Navbar";
import Sidebar from "../../../components/Sidebar/Sidebar";
import { Box, Button, Step, StepLabel, Stepper, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const steps = ["Choose Player", "Video Content", "Get Embed"];

export default function AddContentUnit() {
  const navigate = useNavigate();

  const [activeStep, setActiveStep] = useState(0);

  const [players, setPlayers] = useState([]);

  const [playlist, setPlaylist] = useState([]);

  const [selectedPlayer, setSelectedPlayer] = useState("");

  const [selecedPlaylist, setSelectedPlaylist] = useState("");

  console.log(selectedPlayer, selecedPlaylist);

  const [embedCode, setEmbedCode] = useState(
    `<!DOCTYPE html>
    <html lang="en">
      <head>
        <link rel="stylesheet" href="styles.css" />
        <link href="./videoplayer/build/static/css/main.f955f613.css" rel="stylesheet" />
      </head>
      <script
        defer="defer"
        src="./videoplayer/build/static/js/main.ba67a74a.js"
        playerId="${selectedPlayer}" 
        playlistId="${selecedPlaylist}"
      ></script>
    
      <div id="root">
       
          <div id="container" class="container"></div> <!--Only for In-Slide Ad unit-->
          <div id="firstElement"></div> <!--Only for In-Content Ad unit-->
          <div id="videoplayer"></div>
          <div id="secondElement"></div> <!--Only for In-Content Ad unit-->
      </div>
    </html>
    `
  );

  const [embedCode2, setEmbedCode2] = useState(`<div id="root"></div>`);

  useEffect(() => {
    setEmbedCode(
      `<!DOCTYPE html>
      <html lang="en">
        <head>
          <link rel="stylesheet" href="styles.css" />
          <link href="./videoplayer/build/static/css/main.f955f613.css" rel="stylesheet" />
        </head>
        <script
          defer="defer"
          src="./videoplayer/build/static/js/main.ba67a74a.js"
          playerId="${selectedPlayer}" 
          playlistId="${selecedPlaylist}"
        ></script>
      
        <div id="root">
         
            <div id="container" class="container"></div> <!--Only for In-Slide Ad unit-->
            <div id="firstElement"></div> <!--Only for In-Content Ad unit-->
            <div id="videoplayer"></div>
            <div id="secondElement"></div> <!--Only for In-Content Ad unit-->
        </div>
      </html>
      `
    );
  }, [selectedPlayer, selecedPlaylist]);

  // const getPlayers = async () => {
  //   await axios
  //     .get(`http://64.227.170.236/player/get/post/api/`)
  //     .then(({ data }) => {
  //       console.log(data);
  //       setPlayers(data);
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     });

  //   await axios
  //     .get(`http://64.227.170.236/video/playlist/`)
  //     .then(({ data }) => {
  //       setPlaylist(data);
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     });
  // };

  const getPlayers = async () => {
    await axios
      .get(`/api/player/getPlayers`)
      .then(({ data }) => {
        console.log(data);
        setPlayers(data);
      })
      .catch((err) => {
        console.log(err);
      });

    await axios
      .get(`/api/playlist/getPlaylists`)
      .then(({ data }) => {
        setPlaylist(data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    getPlayers();
  }, []);

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  // const handleFinish = async () => {
  //   await axios
  //     .post(`http://64.227.170.236/content/unit/list/create/`, { player_id: selectedPlayer, playlist_id: selecedPlaylist })
  //     .then(({ data }) => {
  //       navigate("/contentUnits");
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     });
  // };

  const handleFinish = async () => {
    await axios
      .post(`/api/contentUnit/postConentUnit`, { player: selectedPlayer, playlist: selecedPlaylist })
      .then((res) => {
        console.log(res);
        navigate("/contentUnits");
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="addPlayer">
      <Navbar />
      <div className="addPlayer-main">
        <Sidebar />
        <div className="addContentUnit-main-container">
          <span className="title">CREATE SIMPLE CONTENT UNIT</span>

          <Box sx={{ width: "80%", marginTop: "30px", alignItems: "center" }}>
            <Stepper activeStep={activeStep}>
              {steps.map((label, index) => {
                const stepProps = {};
                const labelProps = {};

                return (
                  <Step key={label} {...stepProps}>
                    <StepLabel {...labelProps}>{label}</StepLabel>
                  </Step>
                );
              })}
            </Stepper>
            <div style={{ display: "flex", width: "100%", justifyContent: "center" }}>
              <div className="stepperContainer">
                <div className="stepperMain">
                  {activeStep === 0 && (
                    <div className="stepperMain-step">
                      <Typography sx={{ mt: 2, mb: 1 }}>Select Player</Typography>
                      <select className="playerSelect" onChange={(e) => setSelectedPlayer(e.target.value)}>
                        <option value="" disabled selected hidden>
                          Please Choose...
                        </option>
                        {players.map((e) => {
                          return <option value={e._id}>{e.playerName}</option>;
                        })}
                      </select>
                    </div>
                  )}
                  {activeStep === 1 && (
                    <div className="stepperMain-step">
                      <Typography sx={{ mt: 2, mb: 1 }}>Select Playlist</Typography>
                      <select className="playerSelect" onChange={(e) => setSelectedPlaylist(e.target.value)}>
                        <option value="" disabled selected hidden>
                          Please Choose...
                        </option>
                        {playlist.map((e) => {
                          return <option value={e._id}>{e.title}</option>;
                        })}
                      </select>
                    </div>
                  )}
                  {activeStep === 2 && (
                    <div className="stepperMain-step">
                      <Typography sx={{ mt: 2, mb: 1 }}>Embed Code</Typography>
                      <div className="embedCode">
                        <Typography id="modal-modal-description">{embedCode}</Typography>
                        {/* <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                          {embedCode2}
                        </Typography> */}
                      </div>
                    </div>
                  )}
                </div>

                <Box sx={{ display: "flex", flexDirection: "row", pt: 2 }}>
                  <Button color="inherit" disabled={activeStep === 0} onClick={handleBack} sx={{ mr: 1 }}>
                    Back
                  </Button>
                  <Box sx={{ flex: "1 1 auto" }} />

                  <Button onClick={handleNext}>{activeStep <= steps.length - 2 && "Next"}</Button>

                  <Button onClick={handleFinish}>{activeStep === steps.length - 1 && "Finish"}</Button>
                </Box>
              </div>
            </div>
          </Box>
        </div>
      </div>
    </div>
  );
}
