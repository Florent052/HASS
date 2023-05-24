# Home Assistant Add-on: Nestor

## Installation

Follow these steps to get the add-on installed on your system:

1. Navigate in your Home Assistant frontend to **setting** -> **Add-on Store**.
2. Find the "Nestor" add-on and click it.
3. Click on the "INSTALL" button.

## How to use

1. In the configuration section, set a Last name,first name, your number ,email your Subscriptionx, paiement your billing addresse and which property .

2. Save the configuration.

3. Start the add-on.

4. Check the add-on log output to see the result.

# Configuration

Add-on configuration:

1. In the **setting** on automation section add a new automation.

2. **start with an empty automation**.

3. In the **Triggers** session, add the Triggers you want to add to nestor according to your subscription.

4. In the **condition** session; put the conditions for which nestor must activate.

5. In the **action**, select "Call a Service" then select **Home Assistant Supervisor: Write data to stdin add-on** and finally from  **addon slug** select  on **Nestor**.

6. Change the session to as YAML then add the following code
```yaml
service: hassio.addon_stdin
data:
  addon: local_nestor_addons
  input: nestor
```
7. **Save** the automation 
