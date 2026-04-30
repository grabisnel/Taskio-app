import { User } from "./auth-slice.types"

export type LoginPayload = {
    username: string
    password: string
}

export type LoginResponse = {
    detail: string
    token: string
}

export type BackendUserResponse = Partial<User> & {
    id?: number
}
