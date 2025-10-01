from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


console.print("\n[bold blue]Currículum Vitae[/bold blue]", justify="center")
console.print("[green]Alejandro Zeledón[/green]", justify="center")
console.print("Ingeniería en Sistemas - 2° año", justify="center")
console.print("📧 alejandrozeledon2005105@gmail.com | 📱 81564375 | [link=https://github.com/Alexzel-77]GitHub[/link]\n", justify="center")

edu = Table(title="Educación", show_lines=True)
edu.add_column("Institución", style="cyan", justify="left")
edu.add_column("Detalle", style="white", justify="left")
edu.add_row("Universidad Americana (UAM)", "Ingeniería en Sistemas - 2° año\nPromedio actual: 87\nGraduación prevista: Diciembre 2028")
console.print(edu)


courses = Table(title="Cursos y Certificaciones", show_lines=True)
courses.add_column("Curso", style="yellow")
courses.add_row("Reparación y Mantenimiento de PC – Nivel Básico")
courses.add_row("Reparación y Mantenimiento de PC – Nivel Avanzado")
console.print(courses)


projects = Table(title="Proyectos Académicos Relevantes", show_lines=True)
projects.add_column("Proyecto", style="magenta")
projects.add_row("Desarrollo de programas en Python y C#: lógica, estructuras de datos y algoritmos")
projects.add_row("Colaboración en proyectos universitarios: documentación y trabajo en equipo")
console.print(projects)


skills = Table(title="Habilidades Técnicas", show_lines=True)
skills.add_column("Área", style="cyan")
skills.add_column("Detalle", style="white")
skills.add_row("Lenguajes", "Python, C#")
skills.add_row("Mantenimiento", "Ensamblaje, diagnóstico y reparación de equipos")
skills.add_row("Herramientas", "Visual Studio, Jupyter Notebook")
skills.add_row("Conceptos", "Bases de datos, estructuras de control, POO")
console.print(skills)


soft_skills = Table(title="Habilidades Blandas", show_lines=True)
soft_skills.add_column("Habilidad", style="green")
soft_skills.add_row("Trabajo en equipo y colaboración")
soft_skills.add_row("Resolución de problemas")
soft_skills.add_row("Comunicación efectiva")
soft_skills.add_row("Adaptabilidad y disposición para aprender")
console.print(soft_skills)


langs = Table(title="Idiomas", show_lines=True)
langs.add_column("Idioma", style="blue")
langs.add_column("Nivel", style="white")
langs.add_row("Español", "Nativo")
langs.add_row("Inglés", "B2 (intermedio – avanzado)")
console.print(langs)

console.print(Panel.fit("📌 Participación en actividades académicas y extracurriculares en la UAM\n"
                        "🎯 Interés en soporte técnico, desarrollo de software y análisis de sistemas",
                        title="Información Adicional", border_style="bold red"))


console.print("\n[bold green]Gracias por su tiempo y consideración 😊[/bold green]\n", justify="center")
