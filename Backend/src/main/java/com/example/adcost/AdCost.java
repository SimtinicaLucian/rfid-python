package com.example.adcost;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;

@SpringBootApplication
public class AdCost {

	public static void main(String[] args) {
		SpringApplication.run(AdCost.class, args);
	}

	@Bean
	public WebMvcConfigurer corsConfigurer() {
		return new WebMvcConfigurerAdapter() {
			@Override
			public void addCorsMappings(CorsRegistry registry) {
				registry.addMapping("/alimentari/").allowedOrigins("http://localhost:4200");
				registry.addMapping("/alimentari/delete/number/{number}").allowedOrigins("http://localhost:4200");

			}
		};
	}

}
