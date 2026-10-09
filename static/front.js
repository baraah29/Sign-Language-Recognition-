document.addEventListener("DOMContentLoaded", () => {
    const video = document.getElementById("video");
    const translationText = document.getElementById("translation-text");
    const soundCircle = document.getElementById("sound-circle");

    video.addEventListener("click", () => {
        fetch("/capture", { method: "POST" })
            .then(res => res.json())
            .then(data => {
                translationText.textContent = data.translation || "error";
                soundCircle.classList.add("sound-active");

                setTimeout(() => {
                    soundCircle.classList.remove("sound-active");
                }, 1000);
            })
            .catch(err => console.error("error", err));
    });
});

