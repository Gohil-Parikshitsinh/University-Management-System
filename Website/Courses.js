document.addEventListener("DOMContentLoaded", function () {
    const filters = document.querySelectorAll(".filter");
    const courses = document.querySelectorAll(".course-card");

    filters.forEach(filter => {
        filter.addEventListener("change", () => {
            const level = document.getElementById("levelFilter").value;
            const degree = document.getElementById("degreeFilter").value;
            const field = document.getElementById("fieldFilter").value;

            courses.forEach(course => {
                const courseLevel = course.getAttribute("data-level");
                const courseDegree = course.getAttribute("data-degree");
                const courseField = course.getAttribute("data-field");

                if (
                    (level === "all" || level === courseLevel) &&
                    (degree === "all" || degree === courseDegree) &&
                    (field === "all" || field === courseField)
                ) {
                    course.style.display = "block";
                } else {
                    course.style.display = "none";
                }
            });
        });
    });
});
