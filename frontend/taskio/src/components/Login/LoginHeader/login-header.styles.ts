import { Box, Typography } from "@mui/material"
import { styled } from "@mui/material/styles"

export const StyledBrandIcon = styled(Box)(({ theme }) => ({
    width: 64,
    height: 64,
    borderRadius: theme.spacing(2),
    display: 'grid',
    placeItems: 'center',
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.contrastText,
    boxShadow: theme.shadows[2],
    fontSize: 28,
    fontWeight: 700,
    lineHeight: 1,
}))

export const StyledSubtitle = styled(Typography)(({ theme }) => ({
    color: theme.palette.text.secondary,
    textAlign: 'center',
}))
