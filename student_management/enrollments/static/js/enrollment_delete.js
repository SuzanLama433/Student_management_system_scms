document.addEventListener("DOMContentLoaded", function () {
  const deleteModal = document.getElementById("deleteModal");

  if (deleteModal) {
    deleteModal.addEventListener("show.bs.modal", function (event) {
      const button = event.relatedTarget;
      const name = button.getAttribute("data-name");
      const url = button.getAttribute("data-url");
      const courseName = document.getElementById("courseName");
      const deleteBtn = document.getElementById("deleteBtn");

      if (courseName) {
        courseName.textContent = name;
      }
      if (deleteBtn && url) {
        deleteBtn.href = url;
      }
    });
  }

  const permanentAllModal = document.getElementById("permanentDeleteAllModal");
  if (permanentAllModal) {
    permanentAllModal.addEventListener("show.bs.modal", function (event) {
      const button = event.relatedTarget;
      const name =
        button.getAttribute("data-name") || "all deleted enrollments";
      const url = button.getAttribute("data-url");
      const deleteAllName = document.getElementById("deleteAllCourses");
      const permanentAllDeleteBtn = document.getElementById(
        "permanentAllDeleteBtn",
      );

      if (deleteAllName) {
        deleteAllName.textContent = name;
      }
      if (permanentAllDeleteBtn && url) {
        permanentAllDeleteBtn.href = url;
      }
    });
  }
});
