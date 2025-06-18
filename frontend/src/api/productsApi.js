import api from "../api/axiosConfig.js";

export const getAllProducts = () => {
    return api.get('/product/')
}