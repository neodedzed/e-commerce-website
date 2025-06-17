import { useState } from "react"
import '../styles/login.css'
import { registerUser } from "../userApi"

function Login() {

    const [userDetails, setUserDetails] = useState({
        'username': '',
        'password': '',
    })

    const handleChange = (e) => {
        const {name, value} = e.target

        setUserDetails(prev => ({
            ...prev,
            [name]: value
        }))
    }
    const handleSubmit = async (e) => {
        //Want all details printed here
        e.preventDefault()
        try {
            const res = await registerUser(userDetails)
            console.log(res.data.message)
        } catch(err) {
            console.error('Registration failed', err);
            console.log(err.response?.data?.message || err.message);
        }
    }
    return (
        <>
            <form onSubmit={handleSubmit} className="form-register">
                
                <input 
                type='text'
                name='username' 
                placeholder='username'
                value={userDetails.username}
                onChange={handleChange}
                />
                <input 
                type='text'
                name='password' 
                placeholder="password"
                value={userDetails.password}
                onChange={handleChange}
                />
                <button type="submit">Submit</button>
            </form>
        </>
    )
}

export default Login;