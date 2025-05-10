def inverter_string(string: str) -> str:
  if len(string) == 0:
    return string
  return string[-1] + inverter_string(string[:-1])

print(inverter_string('amor'))