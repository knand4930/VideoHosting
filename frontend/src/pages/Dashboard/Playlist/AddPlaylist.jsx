import React, { useRef, useState } from "react";
import axios from "axios";
import ReactPlayer from "react-player";
import { useEffect } from "react";
import Navbar from "../../../components/Navbar/Navbar";
import Sidebar from "../../../components/Sidebar/Sidebar";
import { Box, Button, Step, StepLabel, Stepper, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import GenerateThumbnail from "./generateThumbnail";

export default function AddPlaylist() {
  const navigate = useNavigate();

  const [title, setTitle] = useState("");

  const [videoArray, setVideoArray] = useState([]);

  const [selectedVideos, setSelectedVideos] = useState([]);

  const handleFinish = async () => {
    // let config = {
    //   method: "post",
    //   maxBodyLength: Infinity,
    //   url: "http://64.227.170.236/video/playlist/",
    //   data: { title: title, video_id: selectedVideos },
    // };

    let config = {
      method: "post",
      maxBodyLength: Infinity,
      url: "/api/playlist/postPlaylist",
      data: { title: title, videos: selectedVideos },
    };

    await axios
      .request(config)
      .then((res) => {
        console.log(res);
        navigate("/playlists");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  // const getVideos = async () => {
  //   await axios
  //     .get(`http://64.227.170.236/video/list`)
  //     .then(async ({ data }) => {
  //       const videoThumbnails = await Promise.all(data.map((video) => GenerateThumbnail(video.file)));

  //       const videosWithThumbnails = data.map((video, i) => ({ ...video, thumbnailUrl: videoThumbnails[i] }));
  //       setVideoArray(videosWithThumbnails);
  //     })
  //     .catch((err) => {
  //       console.log(err);
  //     });
  // };

  const getVideos = async () => {
    await axios
      .get(`/api/video/getVideos`)
      .then(async ({ data }) => {
        const videoThumbnails = await Promise.all(data.map((video) => GenerateThumbnail(video.file)));

        const videosWithThumbnails = data.map((video, i) => ({ ...video, thumbnailUrl: videoThumbnails[i] }));
        setVideoArray(videosWithThumbnails);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    getVideos();
  }, []);

  console.log(selectedVideos);

  const handleSelect = (id) => {
    let exist = selectedVideos.filter((e) => e.toString() === id.toString());

    if (exist.length) {
      let newArray = selectedVideos.filter((e) => e.toString() !== id.toString());
      setSelectedVideos([...newArray]);
    } else {
      setSelectedVideos((prev) => [...prev, id]);
    }
  };

  return (
    <div className="addPlayer">
      <Navbar />
      <div className="addPlayer-main">
        <Sidebar />
        <div className="addContentUnit-main-container">
          <span className="title">Create Playlist</span>

          <div style={{ display: "flex", flexDirection: "column", width: "80%", height: "700px", alignItems: "center" }}>
            <div style={{ marginTop: "20px", display: "flex", width: "100%", alignItems: "center" }}>
              <Typography sx={{ mr: 5, mb: 1 }}>Playlist Name</Typography>
              <input
                style={{ width: "300px", height: "20px", padding: "10px", borderRadius: "10px", border: "1px solid gray" }}
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />
            </div>

            <div
              style={{
                marginTop: "20px",
                display: "flex",
                width: "100%",
                height: "550px",
                flexWrap: "wrap",
                justifyContent: "space-between",
                overflowY: "scroll",
                padding: "20px",
                borderRadius: "10px",
                border: "1px solid black",
              }}
            >
              {videoArray.map((e, index) => {
                return (
                  <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
                    <input type="checkbox" onChange={() => handleSelect(e._id)}></input>
                    <img style={{ height: "60px", width: "60px" }} src={e.thumbnailUrl} alt={e.title} />
                    <h2>{e.title}</h2>
                  </div>
                );
              })}
            </div>

            <Box sx={{ display: "flex", flexDirection: "row", pt: 2 }}>
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  width: "150px",
                  height: "50px",
                  backgroundColor: "red",
                  borderRadius: "10px",
                  color: "white",
                  cursor: "pointer",
                }}
                onClick={handleFinish}
              >
                Save
              </div>
            </Box>
          </div>
        </div>
      </div>
    </div>
  );
}
