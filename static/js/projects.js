const projects = document.querySelectorAll(".project-card");

projects.forEach((project) => {
  project.addEventListener("click", () => {
    const id = project.getAttribute("id");
    window.location.href = `/projects/${id}`;
  });
});
