'use client'

import { Stack } from "@mui/material"
import { LoginCardContainer } from "@/components/Login/LoginCardContainer/LoginCardContainer"
import { LoginContainer } from "@/components/Login/LoginContainer/LoginContainer"
import { LoginForm } from "@/components/Login/LoginForm/LoginForm"
import { LoginHeader } from "@/components/Login/LoginHeader/LoginHeader"

export const LoginFormView = () => {
    return (
        <LoginContainer>
            <LoginCardContainer>
                <Stack spacing={3}>
                    <LoginHeader />
                    <LoginForm />
                </Stack>
            </LoginCardContainer>
        </LoginContainer>
    )
}

export default LoginFormView