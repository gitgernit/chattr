import './Header.css'

let body = document.querySelector('body')

const changeTheme = () => {
  let theme = localStorage.getItem('theme')
  let new_theme = theme === 'light' ? 'dark' : 'light'
  let darkToLight = document.querySelectorAll('.Toastify__toast-theme--dark');
  let lightToDark = document.querySelectorAll('.Toastify__toast-theme--light');

  darkToLight.forEach(div => {
    div.classList.remove('Toastify__toast-theme--dark');
    div.classList.add('Toastify__toast-theme--light');
  });

  lightToDark.forEach(div => {
    div.classList.remove('Toastify__toast-theme--light');
    div.classList.add('Toastify__toast-theme--dark');
  });

  body.setAttribute('theme', new_theme)
  localStorage.setItem('theme', new_theme)
}

const loadTheme = () => {
  body.classList.add('initial-load')
  setTimeout(() => {
    body.classList.remove('initial-load')
  }, 0)
  let theme = localStorage.getItem('theme')

  if (theme) {
    body
      .setAttribute('theme', theme)
  } else {
    changeTheme()
  }
}

loadTheme()


function Header() {
  return (
    <header className="header">
      <span id="app-name">
        chattr
      </span>
      <input type="image" id="theme-button"
             onClick={changeTheme}
             src="/src/assets/theme-button.svg" alt="Theme change"/>
    </header>
  )
}

export default Header
