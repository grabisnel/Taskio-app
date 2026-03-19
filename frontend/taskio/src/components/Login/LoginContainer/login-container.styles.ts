import { Box } from "@mui/material"
import { styled } from "@mui/material/styles"

export const StyledLoginContainer = styled(Box)(({ theme }) => ({
    minHeight: '100dvh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    paddingInline: theme.spacing(2),
    paddingBlock: theme.spacing(4),
    backgroundColor: theme.palette.background.default,
}))
