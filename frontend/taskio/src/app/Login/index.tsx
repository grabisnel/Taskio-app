'use client'

import { Box, Card, useTheme } from "@mui/material"

export const LoginFormView = () => {

    console.log('Passou')

    const theme = useTheme()

    return (
        <Box
            sx={{
                minHeight: '100vh',
                display: 'flex',
                alignItems: 'center',
                border: '1px solid red',
                justifyContent: 'center'
            }}
        >
            <Card 
            sx={{
                minWidth: '200px',
                minHeight: '200px',
                backgroundColor: theme.palette.primary.main
            }}
            >

            </Card>
        </Box>
    )

}

export default LoginFormView