document.addEventListener("DOMContentLoaded", function () {
  const deleteModal = document.getElementById("deleteModal");

  if (deleteModal) {
    deleteModal.addEventListener("show.bs.modal", function (event) {
      const button = event.relatedTarget;
      const name = button.getAttribute("data-name");
      const id = button.getAttribute("data-id");

      document.getElementById("studentName").textContent = name;
      document.getElementById("deleteBtn").href =
        "/students/deleteData/" + id + "/";
    });
  }

  const permaModal = document.getElementById("permanentDeleteModal");
  if (permaModal) {
    permaModal.addEventListener("show.bs.modal", function (event) {
      const button = event.relatedTarget;
      const name = button.getAttribute("data-name");
      const id = button.getAttribute("data-id");

      document.getElementById("deleteName").textContent = name;
      document.getElementById("permanentDeleteBtn").href =
        "/students/deletePerma/" + id + "/";
    });
  }

  const permaAllModal = document.getElementById("permanentDeleteAllModal");
  if (permaAllModal) {
    permaAllModal.addEventListener("show.bs.modal", function () {
      document.getElementById("permanentAllDeleteBtn").href =
        "/students/deleteAll/";
    });
  }
});
