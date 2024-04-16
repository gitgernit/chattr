import './Header.css'

let body = document.querySelector('body')

const changeTheme = () => {
  let theme = localStorage.getItem('theme')
  let new_theme = theme === 'light' ? 'dark' : 'light'
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
      <img id="theme-image"
           src="/src/assets/theme-button.svg" alt="Theme change"
           onClick={changeTheme}/>
    </header>
  )
}

export default Header
