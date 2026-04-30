import { Card } from "@mui/material"
import { styled } from "@mui/material/styles"

export const StyledLoginCardContainer = styled(Card)(({ theme }) => ({
    width: '100%',
    maxWidth: 420,
    borderRadius: theme.spacing(4),
    padding: theme.spacing(3),
    backgroundColor: theme.palette.background.paper,
    boxShadow: theme.shadows[3],
    [theme.breakpoints.up('sm')]: {
        padding: theme.spacing(4),
    },
}))
