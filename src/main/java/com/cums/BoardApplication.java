package com.cums;

import java.io.IOException;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class BoardApplication   {
//implements CommandLineRunner
	public static void main(String[] args) {
		SpringApplication.run(BoardApplication.class, args);
	}

//	@Override
//	public void run(String... args) throws Exception {
////		String pythonExecutable = "myenv/bin/python3"; // macOS/Linux
//		 String pythonExecutable = "myenv\\Scripts\\python"; // Windows
//
//		String scriptPath = "facedetector.py";
//
//		try {
//			ProcessBuilder processBuilder = new ProcessBuilder(pythonExecutable, scriptPath);
//			processBuilder.inheritIO();
//			Process process = processBuilder.start();
//		} catch (IOException e) {
//			e.printStackTrace();
//		}
//	}
}