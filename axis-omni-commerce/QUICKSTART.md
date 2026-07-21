# Quick Start

## 1. Create the repository

1. Unzip the package.
2. Open GitHub Desktop.
3. Select **File → Add local repository**.
4. Choose the extracted `axis-omni-commerce` folder.
5. If GitHub Desktop says it is not a Git repository, choose **create a repository here**.
6. Name it `axis-omni-commerce`.
7. Commit the initial files.
8. Publish the repository.

## 2. Configure the operating policy

Copy:

```text
config/policy.example.yaml
```

to:

```text
config/policy.local.yaml
```

Set:

- allowed platforms;
- maximum experiment spend;
- refund authorization limit;
- prohibited categories;
- human approval thresholds;
- minimum contribution margin;
- maximum acceptable fulfillment time.

Do not commit secrets or live credentials.

## 3. Run the prompt system

Use the complete prompt at:

```text
prompts/AXIS_OMNI_MASTER_PROMPT.md
```

For narrower execution, use the individual role prompts in:

```text
prompts/roles/
```

For specialist routing, use the detailed agent modules in:

```text
prompts/modules/
```

## 4. First proof target

Do not begin with a large catalog. Prove one complete transaction loop:

```text
one authorized supplier
→ one active product
→ one approved platform
→ one compliant listing
→ one real order
→ correct supplier routing
→ tracking returned
→ delivery confirmed
→ actual contribution profit calculated
→ next product recommendation produced
```

## 5. Security

- Store API credentials in environment variables or a secret manager.
- Use least-privilege platform permissions.
- Begin with draft-only or sandbox API access.
- Require human approval for contracts, financial-account connections, material spend, or irreversible actions.
