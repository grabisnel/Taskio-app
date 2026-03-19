import axios from "axios"

const resolvedBaseUrl = (process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000").replace(/\/$/, "")

const defaultApiConfig = {
    withCredentials: true,
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFToken",
}

export const authApi = axios.create({
    baseURL: `${resolvedBaseUrl}/auth/`,
    ...defaultApiConfig,
})

export const userApi = axios.create({
    baseURL: `${resolvedBaseUrl}/user/`,
    ...defaultApiConfig,
})

export function setAuthHeaderToken(token: string | null) {
    const authorizationHeader = token ? `Token ${token}` : null

    ;[authApi, userApi].forEach((apiClient) => {
        if (authorizationHeader) {
            apiClient.defaults.headers.common.Authorization = authorizationHeader
            return
        }

        delete apiClient.defaults.headers.common.Authorization
    })
}
