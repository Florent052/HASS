# Amazon Sidewalk Integration for Home Assistant

This is a custom integration for Home Assistant that provides support for Amazon Sidewalk. With this integration, you can monitor the status of your Sidewalk gateway and receive notifications when the gateway goes offline.

## Installation

To install this integration, you can use the Home Assistant Community Store (HACS) or follow these steps:

1. Clone this repository into the `config/custom_components` directory of your Home Assistant installation:


2. Add the following configuration to your `configuration.yaml` file:


Replace `<your-access-token>` with your Amazon Sidewalk access token.

3. Restart Home Assistant.

## Configuration

The following options can be configured for this integration:

- `access_token`: your Amazon Sidewalk access token (required)

## Usage

Once you have installed and configured this integration, you can use the Home Assistant UI to monitor the status of your Sidewalk gateway and receive notifications when the gateway goes offline.

## Contributing

If you find a bug or have a feature request, please open an issue on GitHub. Pull requests are also welcome!

## License

This integration is licensed under the MIT license. See the [LICENSE](LICENSE) file for more information.
