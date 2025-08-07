# `Position: Human Resources Project Coordinator`  
# `Technical Test` · `Samuel Orduña`

This repository contains the structured solution to the technical test for the **Human Resources Project Coordinator** position, focusing on **process automation**, **data analysis**, and **efficient information management** using tools such as:

- 🐍 **Python 3.10+**  
- 📊 **Pandas**, **NumPy**  
- 📁 Handling of **CSV** and **Excel** files  

---

## Repository Structure

Each exercise was solved in an **independent branch** and documented separately. This approach allows for:

- Clear separation of logic for each solution  
- Easier validation and review  

📄 [Click here to open the technical test in PDF](./Prueba_tecnica_2025.pdf)

---

## Exercise 1 – Name Formatting

This task involved transforming disorganized names into the format:  
**`FirstName(s) LastNamePaternal LastNameMaternal`**, while preserving the `Unique Key` as text.

Two comparative versions were implemented:

| Approach         | File                          | Key Features                                              |
|------------------|-------------------------------|-----------------------------------------------------------|
| Functional       | `ejercicio_1_funcional.py`    | Direct, vectorized logic using `pandas`                   |
| Modular (SOLID)  | `ejercicio_1_SOLID.py`        | Clean separation of responsibilities into small functions |

**Outputs:**
- `resultado_funcional_ejercicio_1.xlsx`  
- `resultado_ejercicio_1_SOLID.xlsx`  

🔍 See comparative analysis in [`ejercicio_1_README.md`](./ejercicio-1/ejercicio_1_README.md)

---

## Exercise 2 – Email Join

This exercise merged email data with the full names from Exercise 1 using the `Unique Key`, ensuring correct data types and performing a **LEFT JOIN**.

**Files involved:**
- `correos.csv`  
- `resultado_funcional_ejercicio_1.xlsx`  

**Generated output:**  
`resultado_ejercicio_2.xlsx`  

📄 See details in [`ejercicio_2_README.md`](./ejercicio-2/ejercicio_2_README.md)

---

## Exercise 3 – Seniority Calculation

This task calculated cumulative seniority of professors based on yearly teaching records, following these rules:

- `1` = full year  
- `0.5` = one semester  
- If **more than 4 years** pass without activity, seniority **resets**

**Files:**
- `matriz_antiguedad.xlsx`  
- `resultado_ejercicio_2.xlsx`  

**Output:**  
`resultado_ejercicio_3.xlsx`  

📄 Full explanation in [`ejercicio_3_README.md`](./ejercicio-3/ejercicio_3_README.md)

---

## Exercise 4 – 2024 Data Update

This exercise updates the seniority matrix with 2024 data and detects new professors.

**Key steps:**
- Cleanup and standardization of headers (`2024` instead of `2,024`)  
- Merging by `Unique Key`  
- Detection of professors **not present** in the original matrix

**Generated files:**
- `matriz_antiguedad_actualizada.xlsx`  
- `profesores_nuevos_2024.xlsx`  

📄 See technical details in [`ejercicio_4_README.md`](./ejercicio-4/ejercicio_4_README.md)

---

## Additional Notes

- All scripts were validated to prevent common issues with numeric keys (`Unique Key`), encodings (`UTF-8`, `Windows-1252`), and file formats.  
- Only **Exercise 1** includes a version following **SOLID principles**, to demonstrate clean and scalable design skills 🙂  
- The rest of the exercises use more direct solutions, assuming low-change environments with simpler modularity needs.

---

## Thank You

Thank you for the opportunity to participate in this process.  
I hope you find the solutions practical, clean, and well-documented.

I'm excited about the possibility of contributing as a **Human Resources Project Coordinator**!

Warm regards,  
**~Samuel Orduña**

[![Thanks <3](https://c.tenor.com/nQXlXRZLWgIAAAAd/tenor.gif)](https://youtu.be/dQw4w9WgXcQ?si=YVCcZr32np6XnFQi)
