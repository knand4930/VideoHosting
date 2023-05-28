export default function generateThumbnail(videoUrl) {
  return new Promise((resolve, reject) => {
    const video = document.createElement("video");
    video.setAttribute("src", videoUrl);
    video.addEventListener("loadeddata", () => {
      const canvas = document.createElement("canvas");
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
      resolve(canvas.toDataURL());
    });
    video.addEventListener("error", () => {
      reject();
    });
  });
}
