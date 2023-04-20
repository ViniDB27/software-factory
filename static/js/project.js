const projects = document.querySelectorAll(".person-avatar");

projects.forEach((project) => {
  project.addEventListener("click", () => {
    const id = project.getAttribute("id");
    window.location.href = `/students/${id ?? "1"}`;
  });
});
