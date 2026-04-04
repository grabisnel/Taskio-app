import axios, { type AxiosInstance, type InternalAxiosRequestConfig } from "axios"

const BASE_URL = (process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000").replace(/\/$/, "")

const BASE_CONFIG = {
    withCredentials: true,
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFToken",
} as const

type TokenProvider = () => string | null

export function createApiClient(path: string, getToken?: TokenProvider): AxiosInstance {
    const client = axios.create({
        baseURL: `${BASE_URL}/${path}/`,
        ...BASE_CONFIG,
    })

    if (getToken) {
        client.interceptors.request.use((config: InternalAxiosRequestConfig) => {
            const token = getToken()
            if (token) {
                config.headers.Authorization = `Token ${token}`
            }
            return config
        })
    }

    return client
}
