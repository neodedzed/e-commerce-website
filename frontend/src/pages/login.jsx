import { useState } from "react"

function Login() {

    const [userDetails, setUserDetails] = useState({
        'username': '',
        'password': '',
        'address': '',
        'phone': '',
    })

    const handleChange = (e) => {
        const {name, value} = e.target

        console.log(e.target, name, value)
        setUserDetails(prev => ({
            ...prev,
            [name]: value
        }))
    }
    const handleSubmit = (e) => {
        //Want all details printed here
        e.preventDefault()
        console.log(userDetails)
    }
    return (
        <>
            <form onSubmit={handleSubmit}>
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
                <input 
                type='text' 
                name='address' 
                placeholder="address"
                value={userDetails.address}
                onChange={handleChange}
                />
                <input 
                type='text' 
                name='phone'
                placeholder="phone"
                value={userDetails.phone}
                onChange={handleChange}
                />

                <button type="submit">Submit</button>
            </form>
        </>
    )
}

export default Login;