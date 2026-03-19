import { User } from "../types/auth-slice.types"
import {
    BackendUserResponse,
    LoginPayload,
    LoginRequestPayload,
    LoginResponse,
} from "../types/auth-service.types"
import { authApi, userApi } from "./auth-api.service"
import { mapUserResponseToAuthUser } from "../auth-mapper"
import { clearSavedAuthToken, saveAuthToken } from "./auth-token.storage"


export async function login(payload: LoginPayload): Promise<LoginResponse> {

    const requestPayload: LoginRequestPayload = {
        username: payload.email,
        password: payload.password,
    }

    const { data } = await authApi.post<LoginResponse>("login/", requestPayload)

    saveAuthToken(data.token)

    return data
}

export async function logout() {
    try {
        await authApi.post("logout/")
        clearSavedAuthToken()
    }
    catch (error) {
        return Promise.reject(error)
}}

export async function getCurrentUser(): Promise<User> {

    const { data } = await userApi.get<BackendUserResponse>("info/")

    return mapUserResponseToAuthUser(data)
}
