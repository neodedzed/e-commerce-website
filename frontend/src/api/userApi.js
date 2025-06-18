import api from "./api/axiosConfig";

export const registerUser = (params) => {
    return api.post('/user/register', params)
}

export const loginUser = (params) => {
    return api.post('/user/login', params)
}

export const healthCheck = () => {
    return api.get('/health')
}