import {useState} from 'react'
import './Homepage.css'

function Homepage() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="upper-center">
        <h1>Chattr</h1>
        <button className="fancy-button"
          onClick={() => setCount((count) => count + 1)}>
          {count}
        </button>
      </div>
    </>
  )
}

export default Homepage
