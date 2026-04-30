'use client'
import { Divider, Stack, TextField } from "@mui/material"
import {
    StyledFormContainer,
    StyledLoginButton,
    StyledPrototypeText,
} from "./login-form.styles"
import { useAuth } from "@/_auth/hooks/useAuth";
import { useForm } from "react-hook-form"
import LoginFormValues from "./login-form.types";

export const LoginForm = () => {
    const {
        loading,
        login, } = useAuth();


    const { register, handleSubmit, formState: { isSubmitting } } = useForm<LoginFormValues>({
        defaultValues: {
            username: "",
            password: "",
        }
    })

    async function onSubmit(data: LoginFormValues) {
        await login(data.username, data.password)
    }

    return (
        <StyledFormContainer onSubmit={handleSubmit(onSubmit)}>
            <Stack spacing={2.5}>
                <TextField
                    label="Username"
                    placeholder="seu_username"
                    variant="outlined"
                    fullWidth
                    {...register("username")}
                />

                <TextField
                    label="Senha"
                    placeholder="••••••••"
                    type="password"
                    variant="outlined"
                    fullWidth
                    {...register("password")}
                />

                <StyledLoginButton
                    type="submit"
                    variant="contained"
                    size="large"
                    fullWidth
                    isLoading={loading || isSubmitting}
                    disabled={loading || isSubmitting}>
                    Entrar agora
                </StyledLoginButton>

                <Divider />

                <StyledPrototypeText variant="body2">💡 Protótipo em desenvolvimento</StyledPrototypeText>
            </Stack>
        </StyledFormContainer>
    )
}
