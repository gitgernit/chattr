function activateChat() {
  let controls = document.querySelector('.controls')
  let chat = document.querySelector('.chat')

  controls.style.display = 'none'
  chat.style.display = 'flex'
}

export { activateChat }
