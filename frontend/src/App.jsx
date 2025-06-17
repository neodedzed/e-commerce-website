import './App.css'
import Login from './pages/login'
import { Routes, Route } from 'react-router-dom'
import Register from './pages/register'
function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Login />}/>
        <Route path='/register' element={<Register />}/>
      </Routes>
      {/* <Login></Login> */}
    </>
  )
}

export default App
