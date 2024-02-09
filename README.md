# MTRparser 

## Overview

The MTRparser is a Python-based tool designed to interpret MTR (My Traceroute) reports, providing a comprehensive analysis of network stability. It evaluates packet loss, latency variations, and overall network performance, offering insights essential for network diagnostics and optimization.

## Features

- **Parse MTR Reports**: Converts raw MTR report data into a structured format for analysis.
- **Network Stability Score**: Calculates a score reflecting the overall stability of the network path based on packet loss and latency variations.
- **Bottleneck Detection**: Identifies potential network bottlenecks by analyzing hop-by-hop latency.
- **Latency Analysis**: Provides average latency across all hops and highlights significant latency fluctuations.

## Installation

Ensure you have Python 3.x installed on your system. This project also requires `numpy` for data analysis.

1. Clone the repository:

git clone https://github.com/annabook21/MTRparser/

2. Navigate to the project directory:

cd mtr-parser

3. Install required dependencies:

pip install numpy

## Usage

To use the MTRparser, you'll need an MTR report saved as a text file. Run the parser with the path to your MTR report file as input:

```shell
python main.py
```

Follow the prompts to input the path to your MTR report file. The tool will display the analysis results, including the overall network stability score, identified bottlenecks, and latency statistics.

**If the MTR report is saved in the same directory as MTRparser, simply enter only the file name such as "mtr_sample.txt" when asked for path information. 

## Contributing

Contributions to the MTRparser project are welcome! To contribute, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Anna Booker 
https://www.linkedin.com/in/annadbooker

Project - https://github.com/annabook21/MTRparser

