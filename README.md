# ROdle (Romanian Wordle)

**Mainly left here for archival purposes.**

This is a clone project of the popular word guessing game we all know and love, but then in Romanian.
The code is based off of [this repository](https://github.com/cwackerfuss/react-wordle).

## Build and run

### To Run Locally:

Clone the repository and perform the following command line actions:

```bash
$> cd react-wordle
$> npm install
$> npm run start
```

### To build/run docker container:

```bash
$> docker build -t game .
$> docker run -d -p 3000:3000 game
```

Open [http://localhost:3000](http://localhost:3000) in browser.
