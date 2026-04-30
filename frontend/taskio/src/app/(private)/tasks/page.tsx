'use client'

import { Box, Card, useTheme } from "@mui/material"

export const TaskView = () => {

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
                backgroundColor: theme.palette.secondary.main
            }}
            >

            </Card>
        </Box>
    )

}

export default TaskView