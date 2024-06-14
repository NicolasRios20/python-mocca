function toggleTheme() {
    // Selecciona el elemento body
    var body = document.getElementsByTagName("body")[0];
    
    // Si el body tiene la clase 'dark-theme', remuévela y agrega 'light-theme'
    if (body.classList.contains("dark-theme")) {
        body.classList.remove("dark-theme");
        body.classList.add("light-theme");
    } else { // Si no, remueve 'light-theme' y agrega 'dark-theme'
        body.classList.remove("light-theme");
        body.classList.add("dark-theme");
    }
}