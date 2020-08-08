import React, { useState, useEffect } from 'react';
import { Container, Typography } from '@material-ui/core'
export default function Homepage(props) {
    const [data, setData] = useState(null);
    useEffect(() => {
        fetch("https://api.fendull.com").then(result => {setData(result)})
    }, [])

    return (
        <Container>
            <Typography>Check out Fendull's stream at <a href="https://twitch.tv/fendull">https://twitch.tv/fendull</a></Typography>
            {data && <Typography>{data}</Typography>}
        </Container>
    )
}