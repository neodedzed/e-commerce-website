import { useEffect, useState } from "react"
import { getAllProducts } from "../api/productsApi"
import AddToCart from "../components/AddToCart"

function Products() {
    let [products, setProducts] = useState([])

    useEffect(() => {
        getAllProducts()
            .then(res => {
                setProducts(() => (products = res.data))
            })
    }, [])
    return (
        <div>
            HERE ARE THE PRODUCTS
            <table>
                <thead>
                    <tr>
                        <th>item</th>
                        <th>quantity</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map(product => (
                        <tr key={product.id}>
                            <td>{product.name}</td>
                            <td>{product.quantity}</td>
                            <td><AddToCart product={product}/></td>
                        </tr>

                        )
                    )}
                </tbody>


            </table>
        </div>
    )
}

export default Products