import { Stack, Typography } from "@mui/material"
import { StyledBrandIcon, StyledSubtitle } from "./login-header.styles"

export const LoginHeader = () => {
    return (
        <Stack spacing={1.5} alignItems="center">
            <StyledBrandIcon>✓</StyledBrandIcon>

            <Typography
                variant="h4"
                component="h1"
                sx={{
                    fontWeight: 700,
                }}
            >
                Taskio
            </Typography>

            <StyledSubtitle variant="body1">✨ Gerencie tarefas com estilo e simplicidade</StyledSubtitle>
        </Stack>
    )
}
