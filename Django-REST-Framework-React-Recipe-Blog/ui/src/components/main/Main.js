import { Box, Container, Stack } from "@mui/material";
import Hero from "../hero/Hero";
import Posts from "../posts/Posts";


const Main = () => {
  return (
    <>
      <Hero />
      <Container>
        <Stack direction={"row"} spacing={1} mt={3}>
          <Box flex={3}>
            <Posts />
          </Box>
          <Box flex={1} display={{ xs: "none", md: "block" }}>
                     </Box>
        </Stack>
      </Container>
    </>
  );
};

export default Main;
