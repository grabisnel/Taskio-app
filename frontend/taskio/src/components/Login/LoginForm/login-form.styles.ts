import { Button, Typography } from "@mui/material"
import { alpha, styled } from "@mui/material/styles"

type StyledLoginButtonProps = {
    isLoading?: boolean
}

export const StyledFormContainer = styled('form')(({ theme }) => ({
    padding: theme.spacing(3),
    borderRadius: theme.spacing(3),
    backgroundColor: alpha(theme.palette.background.default, 0.5),
    border: `1px solid ${theme.palette.divider}`,
}))

export const StyledPrototypeText = styled(Typography)(({ theme }) => ({
    color: theme.palette.text.secondary,
    textAlign: 'center',
}))

export const StyledLoginButton = styled(Button, {
    shouldForwardProp: (prop) => prop !== "isLoading",
})<StyledLoginButtonProps>(({ isLoading = false, theme }) => ({
    paddingBlock: 11,
    fontWeight: 700,
    borderRadius: 999,
    backgroundColor: isLoading ? theme.palette.action.disabled : theme.palette.primary.main
}))
